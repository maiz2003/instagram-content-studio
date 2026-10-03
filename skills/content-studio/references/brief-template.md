# Post brief template

Used by every Content Studio skill. `content-studio` fills it in and saves it as `brief.md` in the package folder. **Required** fields must be known before hooks are written.

```yaml
brand: <slug in brands/>                 # required
post_slug: <short-kebab-name>            # required
publish_date: YYYY-MM-DD                 # required (use "unscheduled" if unknown)
format: reel                             # required: reel | carousel | static | story (Phase 1 is built for reel)
goal: lead                               # required: reach | trust | sale | lead, and must be in the profile's goals_allowed
content_pillar: <one of the profile's content_pillars>   # required
product: <which product/collection from the profile>     # required
key_fact: <the single most important thing this post must land>   # required
target_viewer: <narrow it further than the profile's audience, if useful>
buyer_pain: <the specific pain this post answers>        # strongly recommended for B2B
proof_available: [<real numbers, tests, footage this post can use>]
offer_or_keyword: <DM/WhatsApp/comment keyword and what the viewer gets>
assets_for_this_post: [<locations, people, shots actually available>]
must_include: []
must_avoid: []
notes: ""
test_data: false                         # true → every file in the package is marked TEST DATA
```
