import type { ReactNode } from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';
import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
  return (
    <header className={clsx('hero', styles.heroBanner)}>
      {/* Decorative background shapes */}
      <div className={styles.backgroundShapes}>
        <span className={styles.shape}></span>
        <span className={styles.shape}></span>
        <span className={styles.shape}></span>
      </div>

      <div className="container">
        {/* Main hero title */}
        <Heading as="h1" className={clsx(styles.heroTitle, 'hero__title')}>
          Physical AI & Humanoid Robotics
        </Heading>

        {/* Subtitle with highlights */}
        <p className={clsx(styles.heroSubtitle, 'hero__subtitle')}>
          <span className={styles.highlight}>Explore</span> futuristic robotics and{' '}
          <span className={styles.highlight}>AI systems</span> in style
        </p>

        {/* Hero buttons */}
        <div className={styles.buttons}>
          <Link
            className={clsx('button', styles.gradientButton)}
            to="/docs/intro"
          >
            Start Learning
          </Link>
          <Link
            className={clsx('button', styles.gradientButtonSecondary)}
            to="/insights"
          >
            Read Insights
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home(): ReactNode {
  return (
    <Layout
      title="Physical AI & Humanoid Robotics"
      description="Dive into AI, Humanoid Robotics, and Plug-and-Play systems with a modern dark-themed homepage"
    >
      <HomepageHeader />
      <main>
        {/* Aesthetic feature cards */}
        <HomepageFeatures />
      </main>
    </Layout>
  );
}
