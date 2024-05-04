# Puppet manifest to set up web servers for the deployment of web_static

# Update package repositories
exec { 'apt-update':
  command => '/usr/bin/apt-get update',
}

# Install nginx package
package { 'nginx':
  ensure => 'installed',
}

# Create directories
file { '/data/web_static/releases/test/':
  ensure => 'directory',
  mode   => '0777',
}

file { '/data/web_static/shared/':
  ensure => 'directory',
}

# Create index.html
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => '<html><head></head><body>Holberton School</body></html>',
}

# Create symlink
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test/',
}

# Set ownership
exec { 'set-ownership':
  command => 'chown -R ubuntu:ubuntu /data/',
}

# Add nginx configuration
file_line { 'add-hbnb-static':
  line    => '	location /hbnb_static { alias /data/web_static/current/; }',
  path    => '/etc/nginx/sites-available/default',
  match   => '^.*location \/hbnb_static.*$',
  ensure  => present,
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Start nginx service
service { 'nginx':
  ensure => 'running',
  enable => 'true',
}
