import React from 'react';
import clsx from 'clsx';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import useBaseUrl from '@docusaurus/useBaseUrl';
import styles from './styles.module.css';

const features = [
  {
    title: <>Powered by Python 3</>,
    imageUrl: 'img/sugaroid_python.svg',
    description: (
      <>
        Powered by Natural Language Processing Libraries, <a href="https://spaCy.io" target="_blank">Spacy</a>,
        mulltiplatform modular Artificial Intelligent chatbot made possible for almost all communication 
        platform!
      </>
    ),
  },
  {
    title: <>Modular</>,
    imageUrl: 'img/sugaroid_convo.svg',
    description: (
      <>
        Sugaroid is modular. Features are added as "adapters", and hence the core logic remains constant 
        across implementations. Sugaroid provides a stable Command Line Interface, a Qt powered Graphical User Interface
        for all operating systems, a Discord Bot, IRC bot and a Sugaroid Web Interface all with one same code.
      </>
    ),
  },
  {
    title: <>Fast learning</>,
    imageUrl: 'img/sugaroid_download.svg',
    description: (
      <>
        Sugaroid uses a simple <a href="https://en.wikipedia.org/wiki/Naive_Bayes_classifier" target="_blank">Naive Bayes classifier</a> algorithm, 
        locally trained once and used again. All learned data once trained is stored in a portable SQLite3 Database. 
        So no more client side training.
      </>
    ),
  },
];

function Feature({imageUrl, title, description}) {
  const imgUrl = useBaseUrl(imageUrl);
  return (
    <div className={clsx('col col--4', styles.feature)}>
      {imgUrl && (
        <div className="text--center">
          <img className={styles.featureImage} src={imgUrl} alt={title} />
        </div>
      )}
      <h3>{title}</h3>
      <p>{description}</p>
    </div>
  );
}

function Home() {
  const context = useDocusaurusContext();
  const {siteConfig = {}} = context;
  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="Description will go into a meta tag in <head />">
      <header className={clsx('hero hero--primary', styles.heroBanner)}>
        <div className="container">
          <h1 className="hero__title">{siteConfig.title}</h1>
          <p className="hero__subtitle">{siteConfig.tagline}</p>
          <div className={styles.buttons}>
            <Link
              className={clsx(
                'button button--outline button--secondary button--lg',
                styles.getStarted,
              )}
              to={useBaseUrl('docs/')}>
              Get Started
            </Link>
            <Link
              className={clsx(
                'button button--outline button--secondary button--lg',
                styles.getStarted,
              )}
              to="https://sugaroid.srevinsaju.me">
              Try it now!
            </Link>
          </div>
        </div>
      </header>
      <main>
        {features && features.length > 0 && (
          <section className={styles.features}>
            <div className="container">
              <div className="row">
                {features.map((props, idx) => (
                  <Feature key={idx} {...props} />
                ))}
              </div>
            </div>
          </section>
        )}
      </main>
    </Layout>
  );
}

export default Home;
