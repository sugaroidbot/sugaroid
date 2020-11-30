module.exports = {
  docs: [
    'introduction',
	{
    type: 'category',
    label: 'Getting Started',
    items: [
      {
        type: 'category',
        label: 'Installation',
        items: ['installation', 'installation-pypi', 'installation-requirements' , 'configuration'],
      }
    ],
  },
  'running',
  {
    type: 'category',
    label: 'Interfaces',
    items: ['interfaces-cli', 'interfaces-gui', 'interfaces-django', 'interfaces-ds', 'interfaces-flask'],
  },
  {
    type: 'category',
    label: 'Algorithms',
    items: [
      'algorithm-jsd',
      'algorithm-cos',
      'algorithm-jensen-shannon-distance',
      'naive-bayer-classifier'

      ],
  },
  'adapters','datasets','databases'

  ]
};
