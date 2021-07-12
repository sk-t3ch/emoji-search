export default {
  t3chflicksRootDomain: `https://${process.env.t3chflicksRootDomain}`,
  serviceRootDomain: `https://${process.env.serviceRootDomain}`,
  serviceApiDomain: `https://${process.env.serviceApiDomain}`,
  name: 'Emoji Search',
  slug: 'emoji-search',
  endpoints: [
    {
      path: '/recommendations',
      method: 'POST',
      credits: 1
    }
  ],
  description: 'Find similar emojis to words',
  examples: [
    {
      link: 'https://t3chflicks.org',
      title: 'T3chFlicks Blogs'
    }
  ],
  features: [
    {
      name: 'Interact directly with API',
      items: [
        {
          text: '- Embedable API play component'
        },
        {
          text: '- API Key access'
        }
      ]
    }
  ]
}
