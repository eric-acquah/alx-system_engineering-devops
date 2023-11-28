# Kill a process named killmenow

exec { 'kill_process':
  command => 'pkill -f killmenow',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => 'pgrep -f killmenow',
}
