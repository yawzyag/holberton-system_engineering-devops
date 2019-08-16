# soy un comentario cool
exec {'update':
command  => 'sudo apt update',
provider => shell,
} -> package {'nginx':
ensure => 'installed',
}
-> file { '/etc/nginx/sites-available/default':
ensure => present,
}
-> file_line { 'Edit redirect':
ensure => present,
path   => '/etc/nginx/sites-available/default',
line   => "       location / {
       add_header X-Served-By ${hostname};",
match  => '^\tlocation / {',
}
-> exec { 'restart':
command => '/usr/sbin/service nginx restart',
}
