output "ssh_command" {
  value = "ssh -i ~/.ssh/${var.key_name}.pem ubuntu@${aws_instance.k3s_host.public_ip}"
}

output "kubeconfig_path_hint" {
  value = "/etc/rancher/k3s/k3s.yaml on the EC2 instance"
}
