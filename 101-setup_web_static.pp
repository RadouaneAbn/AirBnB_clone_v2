# This puppet file sets up a web server

exec { '/usr/bin/env apt -y update' : }

-> package {'nginx':
  ensure => 'present',
}

-> file { '/data':
  ensure => 'directory',
}

-> file { '/data/web_static':
  ensure => 'directory',
}

-> file { '/data/web_static/releases':
  ensure => 'directory',
}

-> file { '/data/web_static/shared':
  ensure => 'directory',
}

-> file { '/data/web_static/releases/test':
  ensure => 'directory',
}

$ctn = "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => $ctn,
}

-> file {'/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
}

-> exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}

-> file { '/var/www':
  ensure => 'directory',
}

-> file { '/var/www/html':
  ensure => 'directory',
}

-> file { '/var/www/html/index.html':
  ensure  => 'present',
  content => $ctn,
}

exec { 'nginx_conf':
  command => 'sed -i "29i\ location /hbnb_static/ {\n\t  alias /data/web_static/current/;}" /etc/nginx/sites-enabled/default',
  path    => '/usr/bin:/usr/sbin:/bin:/usr/local/bin',
}

-> service { 'nginx':
  ensure => running,
}
