# cosito puppy
file { '/tmp/holberton':
      ensure  => 'present',
      path    => '/tmp/holberton',
      owner   => 'www-data',
      group   => 'www-data',
      mode    => '0744',
      content => 'I love Puppet',
}