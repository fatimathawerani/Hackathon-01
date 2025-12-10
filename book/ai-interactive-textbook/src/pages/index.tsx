import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';
import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero', styles.heroBanner)}>
      <div className={styles.backgroundShapes}>
        <span className={styles.shape}></span>
        <span className={styles.shape}></span>
        <span className={styles.shape}></span>
      </div>

      <div className="container">
        <Heading as="h1" className={clsx(styles.heroTitle, 'hero__title')}>
          {siteConfig.title}
        </Heading>
        <p className={clsx(styles.heroSubtitle, 'hero__subtitle')}>
          <span className={styles.highlight}>Explore</span> and <span className={styles.highlight}>Learn</span> with Docusaurus
        </p>
        <div className={styles.buttons}>
          <Link
            className={clsx('button', styles.gradientButton)}
            to="/docs/intro">
            Get Started 🚀
          </Link>
          <Link
            className={clsx('button', styles.gradientButtonSecondary)}
            to="/blog">
            Read Blog 📰
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Welcome to ${siteConfig.title}`}
      description="Professional dark-themed homepage for your Docusaurus site">
      <HomepageHeader />
      <main>
        <HomepageFeatures />
      </main>
    </Layout>
  );
}
