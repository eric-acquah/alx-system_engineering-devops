# Maximize the requst processing efficiency of a nginx server.

# Increase the ULIMIT
exec { 'reconfigure-nginx-ULIMIT':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
}

# Restart Nginx
exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/',
  }
