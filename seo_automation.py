from jinja2 import Template

# Define the HTML template as a Jinja2 template string
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{{ description }}">
    <meta name="keywords" content="{{ keywords }}">
    <meta name="author" content="{{ author }}">
    <title>{{ title }}</title>
    
    <!-- Canonical Tag -->
    <link rel="canonical" href="{{ canonical_url }}">
    
    <!-- Open Graph for Social Media -->
    <meta property="og:title" content="{{ og_title }}">
    <meta property="og:description" content="{{ og_description }}">
    <meta property="og:image" content="{{ og_image }}">
    <meta property="og:url" content="{{ og_url }}">
    
    <!-- Schema Markup for Rich Snippets -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": "{{ business_name }}",
        "url": "{{ business_url }}",
        "telephone": "{{ telephone }}",
        "email": "{{ email }}",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "{{ address_locality }}",
            "addressRegion": "{{ address_region }}"
        },
        "serviceArea": {
            "@type": "GeoCircle",
            "geoMidpoint": {
                "@type": "GeoCoordinates",
                "latitude": {{ latitude }},
                "longitude": {{ longitude }}
            },
            "geoRadius": {{ geo_radius }}
        }
    }
    </script>
    
    <!-- CSS for Speed Optimization -->
    <link rel="stylesheet" href="styles.min.css">
    
    <!-- Lazy Loading Images -->
    <style>
        img { loading: lazy; }
    </style>
</head>
<body>
    <header>
        <h1>{{ header_title }}</h1>
    </header>
    <main>
        <section>
            <h2>Why Choose Us?</h2>
            <p>{{ why_choose_us }}</p>
        </section>
        
        <section>
            <h2>Our Services</h2>
            <ul>
                {% for service in services %}
                    <li>{{ service }}</li>
                {% endfor %}
            </ul>
        </section>
    </main>
    
    <!-- Internal Linking Optimization -->
    <footer>
        <nav>
            <ul>
                <li><a href="/about-us">About Us</a></li>
                <li><a href="/services">Our Services</a></li>
                <li><a href="/contact">Contact Us</a></li>
            </ul>
        </nav>
    </footer>
</body>
</html>
"""

# Define the data to populate the template
data = {
    "description": "Professional generator maintenance, repair, and installation services across East Africa. Contact us today!",
    "keywords": "GENERATOR, GENERATORS IN KENYA, GENERATOR MAINTENANCE, GENERATOR REPAIR, GENERATOR LEASE, GENERATOR INSTALLATION, GENERATOR PARTS, USED AND NEW GENERATORS",
    "author": "Emerson Eims Services",
    "title": "Generator Maintenance & Services - Emerson Eims",
    "canonical_url": "https://www.emersoneims.co.ke",
    "og_title": "Professional Generator Services in East Africa",
    "og_description": "Reliable generator maintenance, repair, and leasing services.",
    "og_image": "https://www.emersoneims.co.ke/images/generator-services.jpg",
    "og_url": "https://www.emersoneims.co.ke",
    "business_name": "Emerson Eims Services",
    "business_url": "https://www.emersoneims.co.ke",
    "telephone": "+254XXXXXXXXX",
    "email": "emersoneimservices@gmail.com",
    "address_locality": "Kenya",
    "address_region": "East Africa",
    "latitude": -1.286389,
    "longitude": 36.817223,
    "geo_radius": 1000000,
    "header_title": "Reliable Generator Maintenance & Repair in East Africa",
    "why_choose_us": "We offer expert generator maintenance, repair, leasing, and installation services across Kenya and East Africa.",
    "services": [
        "Routine generator maintenance and servicing",
        "Emergency generator repair services",
        "Generator leasing and rental options",
        "Professional generator installation",
        "Supply of high-quality generator parts"
    ]
}

# Create a Jinja2 template object
template = Template(html_template)

# Render the template with the data
rendered_html = template.render(data)

# Write the rendered HTML to a file
def generate_html():
    with open("seo_optimized_page.html", "w", encoding="utf-8") as file:
        file.write(rendered_html)
    print("SEO-optimized HTML page has been generated successfully!")

# Execute the function
generate_html()