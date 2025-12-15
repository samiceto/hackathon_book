// @ts-check

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.

 @type {import('@docusaurus/plugin-content-docs').SidebarsConfig}
 */
const sidebars = {
  // Book sidebar for the Physical AI & Humanoid Robotics book
  bookSidebar: [
    {
      type: 'category',
      label: 'Part I: Foundations',
      items: [
        'chapter-1-introduction',
        'chapter-2-robot-middleware',
        'chapter-3-human-centered-design',
      ],
      collapsed: false,
    },
    {
      type: 'category',
      label: 'Part II: Simulation Awareness',
      items: [
        'chapter-4-digital-twins',
        'chapter-5-simulation-technologies',
      ],
      collapsed: false,
    },
    {
      type: 'category',
      label: 'Part III: Perception & Cognitive Models',
      items: [
        'chapter-6-sensor-integration',
        'chapter-7-cognitive-models',
        'chapter-8-human-robot-interaction',
      ],
      collapsed: false,
    },
    {
      type: 'category',
      label: 'Part IV: Locomotion & Control Concepts',
      items: [
        'chapter-9-movement-control',
        'chapter-10-balance-stability',
        'chapter-11-path-planning',
      ],
      collapsed: false,
    },
    {
      type: 'category',
      label: 'Part V: Conceptual Capstone',
      items: [
        'chapter-12-integrating-physical-ai',
        'chapter-13-ethics-future',
      ],
      collapsed: false,
    },
  ],
};

export default sidebars;
