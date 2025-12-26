import { themes as prismThemes } from 'prism-react-renderer';
import type { Config } from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'Physical AI & Humanoid Robotics',
  tagline: 'Robots are cool',

  url: 'https://hackathon-01-eta.vercel.app/',
  baseUrl: '/',

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
        },
        blog: {
          showReadingTime: true,
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  // ✅ themeConfig must contain navbar, footer, prism
  themeConfig: {
    navbar: {
  title: 'Physical AI', // fallback
  logo: undefined,      // remove any image logo
  items: [
    { to: '/docs/intro', label: 'Chapters', position: 'left' },
    { label: 'More', position: 'left', items: [{ to: '/about', label: 'About' }, { to: '/contact', label: 'Contact' }] },
    { to: '/login', label: 'Login', position: 'right' },
    { to: '/register', label: 'Signup', position: 'right' },
  ],
},



    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [{ label: 'About the Book', to: '/docs/intro' }],
        },
        {
          title: 'Community',
          items: [
            { label: 'LinkedIn', href: 'https://stackoverflow.com/questions/tagged/docusaurus' },
            { label: 'Discord', href: 'https://discordapp.com/invite/docusaurus' },
            { label: 'X', href: 'https://x.com/docusaurus' },
          ],
        },
        {
          title: 'More',
          items: [
            { label: 'Blog', to: '/blog' },
            { label: 'GitHub', href: 'https://github.com/facebook/docusaurus' },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} My Project, Inc. Built with Docusaurus.`,
    },

    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
