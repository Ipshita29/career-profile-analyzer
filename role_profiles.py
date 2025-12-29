#file that decides which role needs which skill the most 
ROLE_PROFILES = {

    "frontend_developer": {
        "frontend": 0.5,
        "tools": 0.2,
        "backend": 0.1,
        "database": 0.1,
        "data": 0.05,
        "ai_ml": 0.05
    },

    "backend_developer": {
        "backend": 0.45,
        "database": 0.25,
        "tools": 0.2,
        "frontend": 0.1,
        "data": 0.0,
        "ai_ml": 0.0
    },

    "full_stack_developer": {
        "frontend": 0.3,
        "backend": 0.3,
        "database": 0.2,
        "tools": 0.2,
        "data": 0.0,
        "ai_ml": 0.0
    },

    "ai_ml_engineer": {
        "ai_ml": 0.4,
        "data": 0.3,
        "tools": 0.2,
        "database": 0.1,
        "frontend": 0.0,
        "backend": 0.0
    },

    "database_engineer": {
        "database": 0.4,
        "data": 0.3,
        "backend": 0.2,
        "tools": 0.1,
        "frontend": 0.0,
        "ai_ml": 0.0
    }
}
