# install puppet-lint. Version must be 2.5.0
exec { 'puppet-lint':
  command => '/bin/gem install puppet-lint -v 2.5.0',
}
