# puppet manifest to fix termination file
exec { 'fix-wordpress':
  path    => '/bin:/usr/bin',
  command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
}
