from app.route.user.route import Auth, Register
from app.route.profile.route import Profile
from app.route.posts.route import Posts
from app.route.nomenclature.route import Nomenclature
from app.route.movements.route import Movement
from app.route.socnetwork.route import Socnetwork
from app.route.stats.route import Stats


ROUTES = {
    '/register': Register,
    '/auth': Auth,
    '/post': Posts,
    '/nomenclature': Nomenclature,
    '/movements': Movement,
    '/profile/<int:id_user>': Profile,
    '/socnetwork/': Socnetwork,
    '/stats': Stats
}
