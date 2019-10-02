exec { 'fix-wordpress':
  path    => '/bin:/usr/bin:/usr/sbin',
  command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
}
