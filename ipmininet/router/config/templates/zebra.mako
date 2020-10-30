hostname ${node.name}
password ${node.password}

% if node.zebra.logfile:
    log file ${node.zebra.logfile}
% endif

% for section in node.zebra.debug:
    debug zebra ${section}
% endfor

% for itf in node.zebra.interfaces:
interface ${itf.name}
  no shutdown
  description ${itf.description}
  link-detect
  
  link-params 
   enable
	max-bw 1.25e+07
	max-rsv-bw 1.25e+06
	unrsv-bw 0 1.25e+06
	unrsv-bw 1 1.25e+06
	unrsv-bw 2 1.25e+06
	unrsv-bw 3 1.25e+06
	unrsv-bw 4 1.25e+06
	unrsv-bw 5 1.25e+06
	unrsv-bw 6 1.25e+06
	unrsv-bw 7 1.25e+06
	
  <%block name="interface"/>
!
% endfor

% for acl in node.zebra.access_lists:
    % for entry in acl:
${ip_statement(entry.prefix)} ${acl.acl_type} ${acl.name} ${entry.action} ${entry.prefix.with_prefixlen}
    % endfor
% endfor

% for rm in node.zebra.route_maps:
    % for entry in rm:
${rm.describe} ${rm.name} ${entry.action} ${entry.prio}
        % for acl in entry:
  match ${ip_statement(acl.prefix)} address ${acl.acl_type} ${acl.prefix.with_prefixlen}
        % endfor
  <%block name="routemap"/>
    % endfor
!
    % for proto in rm.proto:
ip protocol ${proto} route-map ${rm.name}
    % endfor
% endfor
