import Heading from '@theme/Heading';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'Embodied Intelligence',
    description:
      'Follow the shift from language and simulation toward AI systems that perceive, decide, and act through physical bodies.',
  },
  {
    title: 'Robotics Systems',
    description:
      'Understand the stack behind humanoids: ROS 2, sensors, digital twins, simulators, controllers, and planning loops.',
  },
  {
    title: 'Human Context',
    description:
      'Explore interaction, safety, ethics, and design choices for robots expected to share spaces with people.',
  },
];

function Feature({title, description, index}) {
  const number = String(index + 1).padStart(2, '0');

  return (
    <article className={styles.feature}>
      <div className={styles.featureNumber}>{number}</div>
      <Heading as="h3">{title}</Heading>
      <p>{description}</p>
    </article>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className={styles.featureHeader}>
          <Heading as="h2">What the book connects</Heading>
          <p>
            The chapters are organized around the practical bridge between AI models,
            robotic bodies, and the real environments they operate in.
          </p>
        </div>
        <div className={styles.featureGrid}>
          {FeatureList.map((props, idx) => (
            <Feature key={props.title} index={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
