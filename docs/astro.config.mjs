// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import { unified } from '@astrojs/markdown-remark';
import mermaid from 'astro-mermaid';
import starlightLinksValidator from 'starlight-links-validator';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

// https://astro.build/config
export default defineConfig({
	site: 'https://enzymeml.org',
	trailingSlash: 'always',
	build: { format: 'directory' },
	markdown: {
		// Astro 7 defaults to Sätteri; unified() keeps the remark/rehype pipeline for KaTeX
		processor: unified({ remarkPlugins: [remarkMath], rehypePlugins: [rehypeKatex] }),
	},
	integrations: [
		// must come before starlight
		mermaid({
			autoTheme: true,
			enableLog: false,
			// 'loose' enables the `click node "#anchor"` links in the generated spec graph
			mermaidConfig: { securityLevel: 'loose' },
		}),
		starlight({
			title: 'EnzymeML',
			logo: { src: './src/assets/enzml_logo.png' },
			favicon: '/img/enzml_logo.png',
			social: [
				{ icon: 'github', label: 'GitHub', href: 'https://github.com/EnzymeML/enzymeml-specifications' },
			],
			editLink: {
				baseUrl: 'https://github.com/EnzymeML/enzymeml-specifications/edit/main/docs/',
			},
			customCss: [
				'@fontsource/open-sans/400.css',
				'@fontsource/open-sans/400-italic.css',
				'@fontsource/open-sans/700.css',
				'katex/dist/katex.min.css',
				'./src/styles/custom.css',
			],
			components: {
				Footer: './src/components/Footer.astro',
				// Home page landing hero; falls back to the default hero elsewhere
				Hero: './src/components/landing/Hero.astro',
			},
			plugins: [starlightLinksValidator()],
			sidebar: [
				{ label: 'Home', link: '/' },
				{ label: 'Usage', slug: 'usage' },
				{ label: 'Publications', slug: 'publications' },
				{
					label: 'EnzymeML Data Model',
					items: [{ label: 'Version 2.0', slug: 'versions/v2' }],
				},
				{ label: 'Team', slug: 'team' },
				{ label: 'Validation', slug: 'validation' },
				{ label: 'Learn', items: [{ autogenerate: { directory: 'learn' } }] },
			],
		}),
	],
});
