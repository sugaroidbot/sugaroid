const path = require("path");
const _fs = require("fs");
const remarkMath = require("remark-math");
const rehypeKatex = require("rehype-katex");

module.exports = {
  title: 'Sugaroid',
  tagline: 'Your personal friendly robot assistant',
  url: 'https://www.srevinsaju.me',
  baseUrl: '/sugaroid/',
  favicon: 'img/favicon.ico',
  organizationName: 'srevinsaju', // Usually your GitHub org/user name.
  projectName: 'sugaroid', // Usually your repo name.
  themeConfig: {
    navbar: {
      title: 'Sugaroid',
      logo: {
        alt: 'Sugaroid Logo',
        src: 'img/logo.png',
      },
      items: [
        {
          to: 'docs/',
          activeBasePath: 'docs',
          label: 'Docs',
          position: 'left',
        },
        {to: 'blog', label: 'Blog', position: 'left'},
        {
          href: 'https://github.com/facebook/docusaurus',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Get Started',
              to: 'docs/',
            },
          ],
        },

        {
          title: 'More',
          items: [
            {
              label: 'Blog',
              to: 'blog',
            },
            {
              label: 'GitHub',
              href: 'https://github.com/srevinsaju/sugaroid',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Srevin Saju.`,
    },
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          // It is recommended to set document id as docs home page (`docs/` path).
          homePageId: 'introduction',
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          editUrl:
            'https://github.com/srevinsaju/sugaroid/',
          showLastUpdateTime: true,
          remarkPlugins: [remarkMath],
          rehypePlugins: [[rehypeKatex, {strict: false}]],

          
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          editUrl:
            'https://github.com/srevinsaju/sugaroid/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};
