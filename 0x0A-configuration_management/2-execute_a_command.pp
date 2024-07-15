# creating a manifest using puppet that kills a process name killmenow


exec { 'pkill -f killmenow':
  path   => '/usr/bin:/usr/local/bin:/bin/',
}
