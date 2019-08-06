# cosito puppy
file_line { 'Turn off passwd auth':
  ensure => 'present',
  path => '/etc/ssh/ssh_config',  
  line => 'PasswordAuthentication no',
  match   => 'PasswordAuthentication',
  multiple => true,
}

file_line { 'Declare identity file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton',
  match   => 'IdentityFile',
  ensure => 'present',
  multiple => true,
}