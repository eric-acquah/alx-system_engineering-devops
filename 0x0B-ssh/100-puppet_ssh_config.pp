# make sure dir .ssh exist

file { "${facts['home']}/.ssh":
  ensure => 'directory',
}


# configure ssh file

file { "${facts['home']}/.ssh/config":
  ensure  => 'file',
  content => "Host 107.23.160.42
    User ubuntu
    IdentityFile ${facts['home']}/.ssh/school
    PubkeyAuthentication yes
    PasswordAuthentication no",
}
