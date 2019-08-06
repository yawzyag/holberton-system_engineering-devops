# cosito puppy

file_line { 'Turn off passwd auth':
  ensure => created,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => 'PasswordAuthentication',
}
file_line { 'Declare identity file':
  ensure => created,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentifyFile ~/.ssh/holberton',
  match  => 'IdentifyFile',
}