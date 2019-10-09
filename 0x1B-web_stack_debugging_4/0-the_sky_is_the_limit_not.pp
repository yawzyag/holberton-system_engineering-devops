# puppet manifest to fix termination file
exec { 'fix-nginx':
  path    => '/bin:/usr/bin',
  command => "sed -i 's/15/1024/g' /etc/default/nginx",
}
-> exec { 'restart':
  command => '/usr/sbin/service nginx restart',
}