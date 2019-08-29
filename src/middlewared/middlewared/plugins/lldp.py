from middlewared.schema import Bool, Dict, Str, accepts
from middlewared.service import SystemServiceService


class LLDPModel(sa.Model):
    __tablename__ = 'services_lldp'

    id = sa.Column(sa.Integer(), primary_key=True)
    lldp_intdesc = sa.Column(sa.Boolean())
    lldp_country = sa.Column(sa.String(2))
    lldp_location = sa.Column(sa.String(200))


class LLDPService(SystemServiceService):
    class Config:
        service = 'lldp'
        datastore_prefix = 'lldp_'

    @accepts(Dict(
        'lldp_update',
        Bool('intdesc'),
        Str('country', max_length=2),
        Str('location'),
        update=True
    ))
    async def do_update(self, data):
        """
        Update LLDP Service Configuration.

        `country` is a two letter ISO 3166 country code required for LLDP location support.

        `location` is an optional attribute specifying the physical location of the host.
        """
        old = await self.config()

        new = old.copy()
        new.update(data)

        await self._update_service(old, new)

        return new
