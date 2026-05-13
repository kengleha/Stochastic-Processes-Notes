%BLWN
N = 500;
tau = linspace(-0.5,0.5,500);
No = 1;
B = 5;
mu = 1;

phi = B*No*sinc(2*B*tau) + mu^2;
% y = sin(2*pi*B*tau);
figure
plot(tau,phi,'b', 'LineWidth', 2);hold
plot(tau,zeros(1,N),'k')
plot([1/(2*B) 1/(2*B)],[0, 1],'k--')
plot(tau,ones(1,N)*mu^2,'k--')
xlabel('Time (sec)');ylabel('Amplitude'); title('Sinc Function')
xlabel('\tau (s)')
ylabel('\phi_{xx} (\tau) V^2')
text(1/(2*B),-0.3,'^1/_{2B}')
text(0.25,mu^2+0.2,'\mu^2_x')
set(gca,'Xticklabel',[])
set(gca,'Yticklabel',[])
set(gca,'Xtick',[])
set(gca,'Ytick',[])
axis([-0.5 0.5 -0.5 7])

figure
f = linspace(-10,10,500);
S = No/2*rectangularPulse(-B,B,f);
plot(f,S,'b', 'LineWidth', 2)
hold on
stem(0, mu^2,'b', 'LineWidth', 2)
xlabel('Frequency (Hz)')
ylabel('\Phi_{xx} (f) V^2/Hz')
axis([-10,10,0 1.2])
text(0,1.05,'\mu^2_x')
text(5,-0.03,'B')
text(B+0.1,No/2,'No/2')

set(gca,'Xticklabel',[])
set(gca,'Yticklabel',[])
set(gca,'Xtick',[])
set(gca,'Ytick',[])