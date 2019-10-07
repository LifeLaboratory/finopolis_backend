from app.route.user.route import Auth, Register
from app.route.profile.route import Profile
from app.route.posts.route import Posts


ROUTES = {
    '/register': Register,
    '/auth': Auth,
    '/post': Posts,
    '/profile/<int:id_user>': Profile,

}
