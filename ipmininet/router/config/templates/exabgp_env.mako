%for top_ini in node.exabgp.env.keys():

[exabgp.${top_ini}]
%for item in node.exabgp.env[top_ini].keys():
${item} = ${node.exabgp.env[top_ini][item]}
%endfor
%endfor