# soy un comentario cool
package {'nginx':
ensure => 'installed',
}
-> file { '/etc/nginx/sites-available/default':
            ensure => present,
}
-> file_line { 'Edit redirect':
            ensure  => present,
            path    => '/etc/nginx/sites-available/default',
              line  => "       location / {
	      	   add_header X-Served-By \"${hostname}\";",
              match => '^\tlocation / {',
}
-> exec { 'restart':
            command => '/usr/sbin/service nginx restart',
}
service { 'nginx':
          ensure   => running,
            enable => true,
}

