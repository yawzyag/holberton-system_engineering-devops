# soy un comentario cool
package {'nginx':
ensure => 'installed',
}
file { '/tmp/holberton':
ensure        => 'present',
      path    => '/var/www/html/index.html',
      content => 'Holberton School',
}

file { '/etc/nginx/sites-available/default':
      ensure => present,
}
-> file_line { 'Edit redirect':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => '    listen 80 default_server;
         location /redirect_me {
                  return 301  https://www.youtube.com/watch?v=QH2-TGUlwu4;
          }',
  match  => 'listen 80 default_server',
}
exec { 'restart':
      command => '/usr/sbin/service nginx restart',
}
service { 'nginx':
  ensure => running,
  enable => true,
}
