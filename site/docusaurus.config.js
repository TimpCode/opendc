// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require("prism-react-renderer/themes/github");
const darkCodeTheme = require("prism-react-renderer/themes/dracula");

/** @type {import("@docusaurus/types").Config} */
const config = {
    title: "OpenDC",
    tagline: "Collaborative Datacenter Simulation and Exploration for Everybody",
    url: "https://opendc.org",
    baseUrl: "/",
    onBrokenLinks: "throw",
    onBrokenMarkdownLinks: "warn",
    favicon: "img/favicon.ico",
    organizationName: "atlarge-research",
    projectName: "opendc",

    i18n: {
        defaultLocale: "en",
        locales: ["en"]
    },

    presets: [
        [
            "classic",
            /** @type {import("@docusaurus/preset-classic").Options} */
            ({
                docs: {
                    sidebarPath: require.resolve("./sidebars.js"),
                    editUrl: "https://github.com/atlarge-research/opendc/tree/master/site/"
                },
                theme: {
                    customCss: require.resolve("./src/css/custom.css")
                }
            })
        ]
    ],

    plugins: [
        [
            "content-docs",
            /** @type {import("@docusaurus/plugin-content-docs").Options} */
            ({
                id: "community",
                path: "community",
                routeBasePath: "community",
                editUrl: "https://github.com/atlarge-research/opendc/tree/master/site/",
                sidebarPath: require.resolve("./sidebars.js")
            })
        ]
    ],

    themeConfig:
    /** @type {import("@docusaurus/preset-classic").ThemeConfig} */
        ({
            navbar: {
                title: "OpenDC",
                logo: {
                    alt: "OpenDC logo",
                    src: "img/logo.svg"
                },
                items: [
                    {
                        type: "doc",
                        docId: "intro",
                        position: "left",
                        label: "Learn"
                    },
                    {
                        to: "/community/support",
                        label: "Community",
                        position: "left",
                        activeBaseRegex: `/community/`
                    },
                    {
                        href: "https://github.com/atlarge-research/opendc",
                        label: "GitHub",
                        position: "right"
                    }
                ]
            },
            footer: {
                style: "dark",
                links: [
                    {
                        title: "Learn",
                        items: [
                            {
                                label: "Getting Started",
                                to: "/docs/category/getting-started"
                            },
                            {
                                label: "Tutorials",
                                to: "/docs/category/tutorials"
                            },
                            {
                                label: "Advanced Guides",
                                to: "/docs/category/advanced-guides"
                            }
                        ]
                    },
                    {
                        title: "Community",
                        items: [
                            {
                                label: "Support",
                                to: "/community/support"
                            },
                            {
                                label: "Team",
                                to: "/community/team"
                            },
                            {
                                label: "GitHub Discussions",
                                href: "https://github.com/atlarge-research/opendc/discussions"
                            }
                        ]
                    },
                    {
                        title: "More",
                        items: [
                            {
                                label: "GitHub",
                                href: "https://github.com/atlarge-research/opendc"
                            }
                        ]
                    }
                ],
                copyright: `Copyright © ${new Date().getFullYear()} AtLarge Research. Built with Docusaurus.`
            },
            prism: {
                theme: lightCodeTheme,
                darkTheme: darkCodeTheme
            }
        })
};

module.exports = config;
