# Give user 'holberton' unrestricted access to login and open files.

# Increase hard file limit.
exec { 'hard-file-limit':
  command => "sed -i '/^holberton hard/s/5/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}

# Increase soft file limit.
exec { 'soft-file-limit':
  command => 'sed -i "/^holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
  }
