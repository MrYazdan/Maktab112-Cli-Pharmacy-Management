from core.router import Route, Router, Callback

router = Router(
    Route("Main", description="Maktab 112 - Pharmacy Management", children=[
        Route("Login", callback=Callback('admin.callbacks', 'login')),
        Route("Register", callback=Callback('admin.callbacks', 'register')),
        Route("Panel", children=[
            Route("Login", callback=Callback('admin.callbacks', 'login')),
            Route("Register", callback=Callback('admin.callbacks', 'register')),
            Route("In Panel", children=[
                Route("Login", callback=Callback('admin.callbacks', 'login')),
                Route("Register", callback=Callback('admin.callbacks', 'register')),
            ]),
        ]),
    ])
)
