# puppet manifest to fix termination file
exec { 'fix-hard':
  path    => '/bin:/usr/bin',
  command => "sed -i 's/holberton hard nofile 5/holberton hard nofile 1024/g'\
  /etc/security/limits.conf",
}
-> exec { 'fix-soft':
  path    => '/bin:/usr/bin',
  command => "sed -i 's/holberton soft nofile 4/holberton soft nofile 1024/g'\
  /etc/security/limits.conf",
}
-> exec { 'restart':
  path    => '/bin:/usr/bin:/sbin/',
  command => 'sysctl -p',
}