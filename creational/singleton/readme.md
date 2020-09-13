# Singleton Design Pattern
    - For some component it only make sense to have one copy in the system.
        - Database Repository
        - Object Factory
    - Its because the initializer call is expensive
        - we only do it once.
        - we provide everyone with the same instance.
    - Want to prevent everyone from creating additional copies.
    - Need to take care of lazy instantiation.
        (Only create instance when somebody ask for it)     