from controllers.servers.host_definer import settings

SECRET_DOES_NOT_EXIST = 'Secret {} in namespace {} does not exist'
FAILED_TO_GET_SECRET = 'Failed to get Secret {} in namespace {}, go this error: {}'
CSI_NODE_DOES_NOT_EXIST = 'node {}, do not have csi node'
HOST_DEFINITION_DOES_NOT_EXIST = 'Host definition {} does not exists'
FAILED_TO_GET_CSI_NODES = 'Failed to get csi nodes, got: {}'
FAILED_TO_GET_CSI_NODE = 'Failed to get csi node {}, got: {}'
FAILED_TO_GET_NODES = 'Failed to get nodes, got: {}'
FAILED_TO_GET_STORAGE_CLASSES = 'Failed to get storage classes, got: {}'
FAILED_TO_GET_LIST_OF_HOST_DEFINITIONS = 'Could not get list of hostDefinitions, got: {}'
FAILED_TO_PATCH_HOST_DEFINITION = 'Failed to patch host definition {}, go this error: {}'
FAILED_TO_CREATE_HOST_DEFINITION = 'Failed to create host definition {}, go this error: {}'
FAILED_TO_SET_HOST_DEFINITION_STATUS = 'Failed to set host definition {} status, go this error: {}'
FAILED_TO_CREATE_EVENT_FOR_HOST_DEFINITION = 'Failed to create event for host definition {}, go this error: {}'
FAILED_TO_DELETE_HOST_DEFINITION = 'Failed to delete hostDefinition {}, got: {}'
FAILED_TO_UPDATE_NODE_LABEL = 'Failed to update node {} {} label, got: {}'
FAILED_TO_GET_NODE = 'Failed to get node {}, got: {}'
PATCHING_HOST_DEFINITION = 'Patching host definition: {}'
SET_HOST_DEFINITION_STATUS = 'Set host definition {} status to: {}'
VERIFY_HOST_DEFINITION_USING_EXPONENTIAL_BACKOFF = "Verifying host definition {}, using exponential backoff."\
    " number of retries left [{}]"
SET_HOST_DEFINITION_PHASE_TO_ERROR = 'Set host definition {} phase to error'
SECRET_HAS_BEEN_MODIFIED = 'Managed secret {} in namespace {}, has been modified'
NEW_STORAGE_CLASS = 'New storageClass {}'
CREATING_NEW_HOST_DEFINITION = 'Creating host Definition: {}'
UNDEFINED_HOST = 'Undefine host {} from {} secret in {} namespace'
CREATE_EVENT_FOR_HOST_DEFINITION = 'Creating event : [{}] for host definition: {}'
NEW_KUBERNETES_NODE = 'New Kubernetes node {}, has csi IBM block'
ADD_LABEL_TO_NODE = 'Add {} label to node {}'
REMOVE_LABEL_FROM_NODE = 'Remove {} label from node {}'
FAILED_TO_LIST_DAEMON_SETS = 'Failed to list csi IBM block daemon set, got: {}'
FAILED_TO_LIST_PODS = 'Failed to list csi IBM block pods, got: {}'
FAILED_TO_GET_SECRET_EVENT = 'Failed to get secret {} in namespace {}'
HOST_DEFINITION_IS_NOT_PENDING = "Stopping verifying host definition {}, using exponential backoff,"\
    " because it is not in pending state"
DELETE_HOST_DEFINITION = 'Deleting host definition {}'
ADD_FINALIZER_TO_HOST_DEFINITION = 'Adding finalizer to host definition {}'
REMOVE_FINALIZER_TO_HOST_DEFINITION = 'Removing finalizer from host definition {}'
FAILED_TO_REMOVE_FINALIZER = 'Failed to remove {} finalizer from node'.format(settings.CSI_IBM_FINALIZER)
NODE_ID_WAS_CHANGED = "NodeId was changed for {} node, updating his ports in his definitions,"\
    "old NodeId [{}], new NodeId [{}]"
UPDATE_HOST_DEFINITION_FIELDS_FROM_STORAGE = 'Update host definition {} host from storage fields with {}'
CHECK_NODE_SHOULD_BE_MANAGED_BY_SECRET = 'Check if node {} should be managed by {} secret in {} namespace'
NODE_SHOULD_BE_MANAGED_ON_SECRET = 'Node {} should be managed by {} secret in {} namespace'
NODE_SHOULD_NOT_BE_MANAGED_ON_SECRET = 'Node {} should not be managed by {} secret in {} namespace'
IO_GROUP_CHANGED = 'I/O group changed for node {}, from {} to {}, updating its definitions'
DEFINE_NODE_ON_ARRAYS = 'Defining node {} on arrays {}'
UNDEFINE_NODE_FROM_ARRAYS = 'Undefine node {} from arrays {}'
NODE_WAS_NOT_FOUND_CREATE_NEW_HOST_DEFINITION = "Node {} was not found."\
    "creating a new host definition with initiators: {}"
HOST_CREATED = 'Host {} created on array [{}], with ports [{}], and I/O group [{}]'
NODE_WAS_NOT_FOUND = 'Node {} was not found'
HOST_FOUND = 'host {} found on array'
HOST_PROTOCOL_SHOULD_BE_CHANGE = 'Host {} protocol should be changed'
HOST_PORTS_SHOULD_BE_CHANGE = 'Host {} ports should be changed, new initiators: {}'
HOST_FOUND_WITH_DIFFERENT_INITIATOR = 'host {} found but with different initiators: {}'
CREATED_HOST_DEFINITION = 'Created hostDefinition {}'
READ_SECRET = 'Reading secret {} in namespace {}'
READ_NODE = 'Reading node {}'
CSI_NODES_WITH_IBM_BLOCK_CSI_DRIVER = 'CSINodes with ibm block csi driver: {}'
CHECK_IF_NODE_IS_PART_OF_UPDATE = 'Checking if node {} is part of update'
UPDATED_CSI_NODE_VS_DESIRED = 'CSINode that was updated [{}] and the desired CSINode pods that should be updated [{}]'
CHECK_IF_CSI_NODE_POD_IS_RUNNING = 'Checking if CSINode pod {} is running'
FOUND_HOST_DEFINITION_IN_PENDING_STATE = 'Found hostDefinition {} is in pending state'
CSI_NODE_POD_DELETED_WHILE_HOST_DEFINER_WAS_DOWN = "CSINode pod {} was deleted when the hostDefiner was down,"\
    "deleting all of his hostDefinitions if it allowed"
DETECTED_UNMANAGED_CSI_NODE_WITH_IBM_BLOCK_CSI_DRIVER = 'Detected unmanaged CSINodes with ibm block csi driver: {}'
DETECTED_NEW_MANAGED_CSI_NODE = 'Detected new managed CSINodes [{}], defining it on all the managed secrets'
SECRET_IS_BEING_USED_BY_STORAGE_CLASS = 'Secret {} in namespace {}, it is used by storageClass {}'
SECRET_IS_FROM_TOPOLOGY_TYPE = 'Secret {} in namespace {}, is from topology type'
NEW_MANAGED_SECRET = 'New managed secret {} in namespace {}, defining nodes on it'
DEFINE_NODE_ON_ALL_MANAGED_SECRETS = 'Define node {} on all managed secrets'
DEFINE_NODE_ON_SECRET = 'Defining node {} on secret {} in namespace {}'
GENERATE_REQUEST_FOR_NODE = 'Generating define request for node {}'
COULD_NOT_CHANGE_HOST_PROTOCOL_USING_CHHOST = "Could not change host [{}] protocol using chhost command, "\
    "changing the host protocol by deleting it and creating it again"
