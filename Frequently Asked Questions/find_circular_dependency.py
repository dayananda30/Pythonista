service_dependency = {'Service A': ['Service E', 'Service F'],
                      'Service B': ['Service C'],
                      'Service C': ['Service B'],
                      'Service D': ['Service E'],
                      'Service E': [],
                      'Service F': []
                      }


def find_dependencies(service_name):
    visited_service = []
    if service_name in service_dependency.keys():
        visited_service.append(service_name)
        if service_dependency[service_name]:
            print("Here")
            for serve in service_dependency[service_name]:
                if serve in visited_service:
                    print("Deadlock condition")


find_dependencies("Service B")
