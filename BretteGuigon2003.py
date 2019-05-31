from brian import *

N=500
tau=33*ms
taux=20*ms
sigma=0.02

eqs_input='''
B=2./(1+exp(-2*x))-1 : 1
dx/dt=-x/taux+(2/taux)**.5*xi : 1
'''

eqs='''
dv/dt=(v*I+1)/tau + sigma*(2/tau)**.5*xi : 1
I=0.5+3*p*B : 1
B : 1
p : 1
'''

input=NeuronGroup(1,eqs_input)
neurons=NeuronGroup(N,eqs,threshold=1,reset=0)
neurons.p=linspace(0,1,N)
neurons.v=rand(N)
neurons.B=linked_var(input,'B')

M=StateMonitor(input,'B',record=0)
S=SpikeMonitor(neurons)

run(1000*ms)

subplot(211) # The input
plot(M.times/ms,M[0])
subplot(212)
raster_plot(S)
plot([0,1000],[250,250],'r')
show()
