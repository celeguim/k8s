# k8s

#--- Docker
# docker build -t celeguim/jvminfo:latest .
# docker ps | grep celeguim/jvminfo | awk '{print $1}' | xargs docker logs
# docker run -it -p 8080:8080 -d celeguim/jvminfo

#--- Docker hub push
# docker commit [container id] celeguim/jvminfo
# docker login
# docker push celeguim/jvminfo

#--- Kubernetes install
# sudo vi /etc/yum.repos.d/kubernetes.repo 
	[kubernetes]
	name=Kubernetes
	baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
	enabled=1
	gpgcheck=1
	repo_gpgcheck=1
	gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
	        https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg

sudo yum install -y kubelet kubeadm kubectl
sudo sed -i 's/cgroup-driver=systemd/cgroup-driver=cgroupfs/g' /etc/systemd/system/kubelet.service.d/10-kubeadm.conf
sudo systemctl daemon-reload
sudo systemctl restart kubelet
sudo kubeadm init --apiserver-advertise-address=192.168.1.57 --pod-network-cidr=192.168.1.0/16

#--- Start
minikube start --vm-driver virtualbox ///// DON'T USE SUDO /////
# kubectl get nodes
# DEPRECATED kubectl run jvminfo-app --image=celeguim/jvminfo --port=80 --replicas=2
# NAO CRIA O DEPLOY kubectl run jvminfo-app --generator=run-pod/v1 --image=celeguim/jvminfo --port=80 --replicas=2
# kubectl get pods -o wide
# kubectl expose deployment jvminfo-app --type=LoadBalancer
# kubectl expose deployment jvminfo-app --type=NodePort
# kubectl get service jvminfo-app
# minikube service jvminfo-app --url
# kubectl delete pods,services,deploy jvminfo-app
# minikube addons enable ingress
# kubectl create -f deploy.yaml

#--- Kubernetes uninstall 
sudo kubeadm reset
sudo yum autoremove kubeadm kubectl kubelet kubernet-cni
sudo yum autoremove
sudo rm -rf ~/.kube



--- cAdvisor pra monitorar
# docker run \
  --volume=/:/rootfs:ro \
  --volume=/var/run:/var/run:rw \
  --volume=/sys:/sys:ro \
  --volume=/var/lib/docker/:/var/lib/docker:ro \
  --publish=8080:8080 \
  --detach=true \
  --name=cadvisor \
  google/cadvisor:latest
  
