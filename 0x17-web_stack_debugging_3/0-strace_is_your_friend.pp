# A puppet script to correct the wordpress settings file
# and replace the extension from phpp to php
$setting_file = '/var/www/html/wp-settings.php'
exec { 'replace_extention':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' ${setting_file}",
  path    => ['/bin', '/usr/bin']
}
