# -*- mode: ruby -*-
# vim: set ft=ruby :

MACHINES=[
  {
    :hostname => "flask",
    :ip => "10.0.1.4",
    :box_name => "centos/8"
  }
]

Vagrant.configure(2) do |config|
    MACHINES.each do |machine|
        config.vm.define machine[:hostname] do |node|
            node.vm.box = machine[:box_name]
            node.vm.hostname = machine[:hostname]
            node.vm.network "private_network", ip: machine[:ip]
            node.vm.provider "virtualbox" do |v|
              v.memory = 512
            end
            node.vm.provision "ansible" do |ansible|
              ansible.playbook = "Playbook_deploy_web.yml"
              ansible.tags = "all"
            end
        end
    end
end
