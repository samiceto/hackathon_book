import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import HomepageFeatures from '@site/src/components/HomepageFeatures';
import styles from './index.module.css';

const chapterLinks = [
  {
    title: 'Foundations',
    description: 'Start with embodied intelligence, robot middleware, and human-centered design.',
    to: '/docs/chapter-1-introduction',
  },
  {
    title: 'Simulation to Reality',
    description: 'Connect digital twins, simulation environments, sensors, and cognitive models.',
    to: '/docs/chapter-4-digital-twins',
  },
  {
    title: 'Humanoid Motion',
    description: 'Study movement control, balance, stability, and path planning for walking bodies.',
    to: '/docs/chapter-9-movement-control',
  },
];

function SystemMap() {
  return (
    <div className={styles.systemMap} aria-label="Physical AI learning map">
      <div className={styles.robotFrame}>
        <div className={styles.robotHead}>
          <span />
          <span />
        </div>
        <div className={styles.robotTorso}>
          <div className={styles.coreRing}>AI</div>
          <div className={styles.signalLine} />
          <div className={styles.signalLineAlt} />
        </div>
        <div className={styles.robotBase} />
      </div>
      <div className={`${styles.mapNode} ${styles.nodeBrain}`}>Cognition</div>
      <div className={`${styles.mapNode} ${styles.nodeWorld}`}>World Model</div>
      <div className={`${styles.mapNode} ${styles.nodeSensors}`}>Sensors</div>
      <div className={`${styles.mapNode} ${styles.nodeMotion}`}>Motion</div>
      <div className={`${styles.mapNode} ${styles.nodeEthics}`}>Ethics</div>
    </div>
  );
}

function HomepageHeader() {
  return (
    <header className={styles.hero}>
      <div className="container">
        <div className={styles.heroGrid}>
          <div className={styles.heroCopy}>
            <p className={styles.kicker}>Conceptual guide for embodied intelligence</p>
            <Heading as="h1" className={styles.heroTitle}>
              Physical AI & Humanoid Robotics
            </Heading>
            <p className={styles.heroSubtitle}>
              Learn how simulated brains become walking, sensing, human-aware machines through
              robotics middleware, digital twins, control, cognition, and responsible design.
            </p>
            <div className={styles.heroActions}>
              <Link className={styles.primaryAction} to="/docs/intro">
                Start reading
              </Link>
              <Link className={styles.secondaryAction} to="/docs/chapter-1-introduction">
                Open chapter 1
              </Link>
            </div>
          </div>
          <SystemMap />
        </div>
      </div>
    </header>
  );
}

function ReadingPaths() {
  return (
    <section className={styles.readingPaths}>
      <div className="container">
        <div className={styles.sectionHeader}>
          <Heading as="h2">Choose a path through the book</Heading>
          <p>
            Move from ideas to systems: perception, simulation, interaction, control, and
            deployment choices that shape modern humanoid robots.
          </p>
        </div>
        <div className={styles.pathGrid}>
          {chapterLinks.map((chapter) => (
            <Link className={styles.pathCard} to={chapter.to} key={chapter.title}>
              <span>{chapter.title}</span>
              <p>{chapter.description}</p>
            </Link>
          ))}
        </div>
      </div>
    </section>
  );
}

export default function Home() {
  const {siteConfig} = useDocusaurusContext();

  return (
    <Layout
      title={siteConfig.title}
      description="A conceptual book on Physical AI and Humanoid Robotics, from simulation to embodied robot behavior.">
      <HomepageHeader />
      <main>
        <ReadingPaths />
        <HomepageFeatures />
      </main>
    </Layout>
  );
}
