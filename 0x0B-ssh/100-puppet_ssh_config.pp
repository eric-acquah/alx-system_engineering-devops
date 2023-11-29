# configure ssh file

file { "/etc/ssh/ssh_config":
  ensure  => 'present',
  content => "Host 107.23.160.42
    User ubuntu
    IdentityFile ~/.ssh/school
    PubkeyAuthentication yes
    PasswordAuthentication no",
}
