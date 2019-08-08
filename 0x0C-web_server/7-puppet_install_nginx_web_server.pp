# soy un comentario cool
package {'nginx':
ensure => present,

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
                  return 301 https://www.youtube.com/;
          }',
  match  => 'listen 80 default_server',
}
service { 'nginx':
  ensure => running,
  enable => true,
}
exec { 'restart':
      command => '/usr/sbin/service nginx restart',
}