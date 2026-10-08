import { createMarkdownProcessor } from '@astrojs/markdown-remark';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

// one shared processor (shiki init is expensive), same math support as the site's markdown
export const markdown = createMarkdownProcessor({
	remarkPlugins: [remarkMath],
	rehypePlugins: [rehypeKatex],
	// both themes as CSS vars; Chat.astro picks one per Starlight theme
	shikiConfig: { themes: { light: 'github-light', dark: 'github-dark' }, defaultColor: false },
});
