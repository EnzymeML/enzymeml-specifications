// Converts md-models `mk-docs` output (versions/*.md, written by `md-models pipeline` via ../gen.toml)
// into Starlight-compatible markdown under src/content/docs/versions/. Never edit the output by hand.
// ponytail: regex over a fixed template; switch to an md-models `starlight` template if the template grows.
import assert from 'node:assert/strict';
import { mkdirSync, readFileSync, readdirSync, writeFileSync } from 'node:fs';

const SRC = new URL('../versions/', import.meta.url);
const OUT = new URL('../src/content/docs/versions/', import.meta.url);
const EDIT = 'https://github.com/EnzymeML/enzymeml-specifications/edit/main/specifications/';

export function convert(md, name) {
	md = md.replace(/^---\n[\s\S]*?\n---\n/, ''); // MkDocs `hide:` frontmatter (nav = false)
	const title = md.match(/^# (.+)$/m)?.[1] ?? 'Model Reference';
	md = md.replace(/^# .+\n/m, '');

	// `??? type "Title"` + 4-space indented body  ->  <details>
	md = md.replace(/^\?\?\?\+? \w+(?: "(.*)")?\n((?:(?: {4}.*)?\n)+)/gm, (_, summary = 'Details', body) =>
		`<details>\n<summary>${summary}</summary>\n\n${body.replace(/^ {4}/gm, '').trimEnd()}\n\n</details>\n\n`
	);

	// template glues option bullets onto one line: "- `Default`: 2.0- `Pattern`: ..."
	md = md.replace(/(\S)- `(\w+)`:/g, '$1\n- `$2`:');

	const fm = [
		'---',
		`title: ${JSON.stringify(title)}`,
		`editUrl: ${EDIT}${name}`,
		'tableOfContents:',
		'  maxHeadingLevel: 3',
		'---',
		'',
	].join('\n');
	return fm + md.trimStart();
}

function check() {
	const sample = [
		'# EnzymeML V2',
		'',
		'Intro.',
		'',
		'??? quote "Graph"',
		'    ``` mermaid',
		'    flowchart TB',
		'        a(A) --> b(B)',
		'',
		'        click a "#a" "Go to A"',
		'    ```',
		'',
		'',
		'## Types',
		'- `Default`: 2.0- `Pattern`: "^x$"',
		'',
	].join('\n');
	const out = convert(sample, 'v2.md');
	assert.match(out, /^---\ntitle: "EnzymeML V2"\neditUrl: .*specifications\/v2\.md\n/);
	assert.ok(!out.includes('# EnzymeML V2'), 'h1 moved to frontmatter');
	assert.ok(!out.includes('???'), 'details converted');
	assert.ok(
		out.includes('<details>\n<summary>Graph</summary>\n\n``` mermaid\nflowchart TB\n    a(A) --> b(B)\n\n    click a'),
		'body dedented by one level'
	);
	assert.ok(out.includes('```\n\n</details>\n\n## Types'), 'details closed before next section');
	assert.ok(out.includes('- `Default`: 2.0\n- `Pattern`: "^x$"'), 'glued options split');
	assert.ok(convert('---\nhide:\n  - navigation\n---\n# T\n', 'x.md').startsWith('---\ntitle: "T"'));
	console.log('convert-spec: self-check ok');
}

if (process.argv.includes('--check')) check();

mkdirSync(OUT, { recursive: true });
for (const name of readdirSync(SRC).filter((f) => f.endsWith('.md'))) {
	writeFileSync(new URL(name, OUT), convert(readFileSync(new URL(name, SRC), 'utf8'), name));
	console.log(`convert-spec: versions/${name} -> src/content/docs/versions/${name}`);
}
