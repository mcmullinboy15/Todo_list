error_resp = {
    'error_no_command':
        {
            'error': 'No command variable was provided',
            'usage': 'Please provide a one of the following variables '
                     'determining how you would like to edit the database: \n'
                     '[ Object is based on the url ]',
            'possible boolean variables':
                {
                    'create': 'creates a new object',
                    'edit': 'edits object with given id',
                    'link': 'links one object to its parent or child\n'
                            'ex: Moving a task from one list to another',
                    'delete': 'deletes object provided',
                    'add_cont': 'adds an array [to be implemented] of contributors to the object'
                }
        }
    ,
    'error_type': {
        'SYSTEM_TYPE_ERROR': 'Andrew you dun messed up!!',
        'error': 'The system was not able to determine what type object you desired to manipulate'
    }
    ,
    'forgienkey_error': {
        'FORGIENKEY_NOTFOUND': 'Object couldn\'t be Found because:'
    }
}