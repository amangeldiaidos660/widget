"""
Management command to populate the database with realistic data for ARRFR system
"""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from feedback_app.models import Project, Ticket, Comment, Attachment
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate database with realistic data for ARRFR Financial Regulator system'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting database population...'))

        # Clear existing data
        self.stdout.write(self.style.WARNING('Clearing existing data...'))
        Comment.objects.all().delete()
        Attachment.objects.all().delete()
        Ticket.objects.all().delete()
        Project.objects.all().delete()
        User.objects.filter(is_superuser=False).delete()
        self.stdout.write(self.style.SUCCESS('✓ Old data cleared'))

        # Create superuser
        if not User.objects.filter(username='root').exists():
            User.objects.create_superuser('root', 'admin@finreg.kz', '123')
            self.stdout.write(self.style.SUCCESS('✓ Created superuser: root/123'))

        # Create staff users
        users_data = [
            ('b.nurlan', 'Б. Нұрлан', 'b.nurlan@finreg.kz', 'Backend Developer'),
            ('a.aigul', 'А. Айгуль', 'a.aigul@finreg.kz', 'Frontend Developer'),
            ('k.yerzhan', 'К. Ержан', 'k.yerzhan@finreg.kz', 'DevOps Engineer'),
            ('t.madina', 'Т. Мадина', 't.madina@finreg.kz', 'QA Engineer'),
            ('s.aman', 'С. Аман', 's.aman@finreg.kz', 'Full Stack Developer'),
            ('a.amangeldi', 'А. Амангельди', 'a.amangeldi@finreg.kz', 'System Administrator'),
        ]

        users = {}
        for username, full_name, email, role in users_data:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, email=email, password='123')
                user.first_name = full_name
                user.save()
                users[username] = user
                self.stdout.write(f'✓ Created user: {username}')
            else:
                users[username] = User.objects.get(username=username)

        # Create projects
        projects_data = [
            {
                'name': 'Портал АРРФР (Production)',
                'slug': 'arrfr-portal-prod',
                'is_active': True,
            },
            {
                'name': 'Система отчетности участников рынка',
                'slug': 'market-reporting-system',
                'is_active': True,
            },
            {
                'name': 'Личный кабинет инвестора',
                'slug': 'investor-personal-account',
                'is_active': True,
            },
            {
                'name': 'API Gateway для внешних систем',
                'slug': 'external-api-gateway',
                'is_active': True,
            },
            {
                'name': 'Мобильное приложение АРРФР',
                'slug': 'arrfr-mobile-app',
                'is_active': False,
            },
        ]

        projects = {}
        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                slug=project_data['slug'],
                defaults=project_data
            )
            projects[project_data['slug']] = project
            status = 'Created' if created else 'Exists'
            self.stdout.write(f'✓ {status} project: {project.name}')

        # Realistic incident descriptions for financial regulator
        incidents_data = [
            {
                'title': 'Тайм-аут подключения к API Gateway на PROD',
                'description': 'Производственная среда возвращает 504 Gateway Timeout при запросах к эндпоинту /api/v1/reports. Проблема началась после деплоя версии 2.3.4. Затронуты все клиенты, использующие автоматическую отправку отчетов.',
                'status': 'new',
                'priority': 'high',
                'project': 'external-api-gateway',
                'reporter_name': 'Система мониторинга Zabbix',
                'reporter_email': 'monitoring@finreg.kz',
                'page_url': 'https://api.finreg.kz/v1/reports',
                'console_logs': '{"error": "Gateway Timeout", "status": 504, "timestamp": "2025-12-07T10:23:45Z"}',
                'network_errors': '[{"type": "timeout", "endpoint": "/api/v1/reports", "duration": 30000}]',
                'js_errors': '[]',
                'days_ago': 0,
            },
            {
                'title': 'Ошибка при загрузке финансовых отчетов в Excel формате',
                'description': 'Пользователи не могут скачать сводные отчеты в формате XLSX. При нажатии на кнопку "Экспорт в Excel" появляется ошибка 500. Проблема затрагивает только отчеты за последний квартал 2025 года.',
                'status': 'in_progress',
                'priority': 'high',
                'project': 'market-reporting-system',
                'reporter_name': 'М. Жанар',
                'reporter_email': 'm.zhanar@halykfinance.kz',
                'page_url': 'https://reports.finreg.kz/quarterly/export',
                'console_logs': '{"error": "Internal Server Error", "trace": "ExcelWriter failed at cell B142"}',
                'network_errors': '[{"status": 500, "endpoint": "/export/xlsx"}]',
                'js_errors': '[]',
                'days_ago': 1,
            },
            {
                'title': 'Медленная загрузка дашборда аналитики на UAT',
                'description': 'На тестовой среде дашборд с графиками и аналитикой загружается более 10 секунд. В production время загрузки составляет 2-3 секунды. Возможно, проблема связана с неоптимизированными SQL запросами или отсутствием индексов.',
                'status': 'in_progress',
                'priority': 'medium',
                'project': 'arrfr-portal-prod',
                'reporter_name': 'QA Team',
                'reporter_email': 'qa@finreg.kz',
                'page_url': 'https://uat.finreg.kz/analytics/dashboard',
                'console_logs': '{"query_time": 8234, "queries_count": 47}',
                'network_errors': '[]',
                'js_errors': '[{"message": "Chart rendering took 3421ms"}]',
                'days_ago': 2,
            },
            {
                'title': 'Недоступность базы данных PostgreSQL - Connection Pool Exhausted',
                'description': 'На PROD сервере исчерпан пул подключений к PostgreSQL. База данных возвращает ошибку "FATAL: sorry, too many clients already". Текущий лимит connections = 100, активных подключений 98-100. Требуется увеличение лимита или оптимизация работы с соединениями.',
                'status': 'new',
                'priority': 'critical',
                'project': 'market-reporting-system',
                'reporter_name': 'Система мониторинга',
                'reporter_email': 'devops@finreg.kz',
                'page_url': 'N/A (Database Server)',
                'console_logs': '{"error": "FATAL: sorry, too many clients already", "max_connections": 100}',
                'network_errors': '[]',
                'js_errors': '[]',
                'days_ago': 0,
            },
            {
                'title': 'Ошибка валидации БИН при регистрации новой организации',
                'description': 'Форма регистрации участника финансового рынка не принимает корректные БИН (Бизнес Идентификационный Номер). Валидация выдает ошибку "Некорректный формат БИН" даже для валидных 12-значных номеров. Проблема появилась после обновления библиотеки валидации.',
                'status': 'in_progress',
                'priority': 'high',
                'project': 'arrfr-portal-prod',
                'reporter_name': 'Е. Сауле',
                'reporter_email': 'e.saule@freedom-finance.kz',
                'page_url': 'https://portal.finreg.kz/registration/organization',
                'console_logs': '{"error": "Invalid BIN format", "input": "123456789012"}',
                'network_errors': '[]',
                'js_errors': '[{"field": "bin", "message": "Validation failed"}]',
                'days_ago': 3,
            },
            {
                'title': 'Некорректное отображение графиков в Internet Explorer 11',
                'description': 'Графики на странице аналитики не загружаются в браузере IE11. Пользователи видят пустые блоки вместо диаграмм. Проблема связана с отсутствием поддержки ES6+ синтаксиса в старых браузерах.',
                'status': 'resolved',
                'priority': 'low',
                'project': 'arrfr-portal-prod',
                'reporter_name': 'Н. Асхат',
                'reporter_email': 'n.askhat@government.kz',
                'page_url': 'https://portal.finreg.kz/analytics',
                'console_logs': '[]',
                'network_errors': '[]',
                'js_errors': '[{"error": "Object doesn\'t support property or method \'includes\'", "browser": "IE 11"}]',
                'days_ago': 15,
            },
            {
                'title': 'Сбой в системе двухфакторной аутентификации',
                'description': 'Пользователи не получают SMS с кодами подтверждения при входе в систему. Проблема затрагивает абонентов всех операторов связи. Интеграция с SMS-шлюзом возвращает timeout. Возможна проблема на стороне провайдера SMS услуг.',
                'status': 'in_progress',
                'priority': 'critical',
                'project': 'arrfr-portal-prod',
                'reporter_name': 'Служба поддержки',
                'reporter_email': 'support@finreg.kz',
                'page_url': 'https://portal.finreg.kz/login/2fa',
                'console_logs': '{"error": "SMS Gateway timeout", "provider": "KazSMS", "timeout": 5000}',
                'network_errors': '[{"endpoint": "https://sms.kazsms.kz/send", "status": "timeout"}]',
                'js_errors': '[]',
                'days_ago': 0,
            },
            {
                'title': 'Утечка памяти в микросервисе обработки отчетов',
                'description': 'Микросервис report-processor постепенно увеличивает потребление RAM. За 8 часов работы использование памяти растет с 512MB до 4GB, после чего сервис падает с ошибкой OOM (Out of Memory). Требуется профилирование и поиск утечек памяти.',
                'status': 'new',
                'priority': 'high',
                'project': 'market-reporting-system',
                'reporter_name': 'DevOps Team',
                'reporter_email': 'devops@finreg.kz',
                'page_url': 'N/A (Microservice)',
                'console_logs': '{"error": "OutOfMemoryError", "heap_usage": "4096MB/4096MB"}',
                'network_errors': '[]',
                'js_errors': '[]',
                'days_ago': 1,
            },
            {
                'title': 'Ошибка сертификата SSL для поддомена api.finreg.kz',
                'description': 'SSL сертификат для api.finreg.kz истекает через 5 дней. Браузеры начнут показывать предупреждения о безопасности. Необходимо продление сертификата и его установка на балансировщик нагрузки.',
                'status': 'in_progress',
                'priority': 'high',
                'project': 'external-api-gateway',
                'reporter_name': 'Security Scanner',
                'reporter_email': 'security@finreg.kz',
                'page_url': 'https://api.finreg.kz',
                'console_logs': '{"warning": "Certificate expires in 5 days", "expiry_date": "2025-12-12"}',
                'network_errors': '[]',
                'js_errors': '[]',
                'days_ago': 2,
            },
            {
                'title': 'Проблема с синхронизацией данных между PROD и DR',
                'description': 'Резервный дата-центр (Disaster Recovery) отстает от основного на 2 часа. Репликация данных PostgreSQL работает некорректно. В случае аварии основного ДЦ возможна потеря данных за последние 2 часа.',
                'status': 'new',
                'priority': 'critical',
                'project': 'arrfr-portal-prod',
                'reporter_name': 'Infrastructure Team',
                'reporter_email': 'infrastructure@finreg.kz',
                'page_url': 'N/A (Database Replication)',
                'console_logs': '{"lag": "7200 seconds", "primary": "almaty-dc1", "replica": "shymkent-dr"}',
                'network_errors': '[]',
                'js_errors': '[]',
                'days_ago': 0,
            },
            {
                'title': 'Некорректный расчет комиссий в калькуляторе инвестора',
                'description': 'Калькулятор доходности в личном кабинете инвестора показывает неверные комиссии брокера. Фактическая комиссия 0.3%, а система рассчитывает 0.5%. Ошибка в формуле расчета.',
                'status': 'resolved',
                'priority': 'medium',
                'project': 'investor-personal-account',
                'reporter_name': 'Д. Алия',
                'reporter_email': 'd.aliya@gmail.com',
                'page_url': 'https://investor.finreg.kz/calculator',
                'console_logs': '{"calculated_fee": 0.005, "expected_fee": 0.003}',
                'network_errors': '[]',
                'js_errors': '[]',
                'days_ago': 20,
            },
            {
                'title': 'Падение Nginx балансировщика на PROD',
                'description': 'Nginx балансировщик перезапустился из-за ошибки сегментации (segmentation fault). Простой составил 3 минуты. Необходимо расследование причин и обновление до стабильной версии.',
                'status': 'resolved',
                'priority': 'critical',
                'project': 'arrfr-portal-prod',
                'reporter_name': 'Система мониторинга',
                'reporter_email': 'alerts@finreg.kz',
                'page_url': 'N/A (Load Balancer)',
                'console_logs': '{"error": "Segmentation fault", "nginx_version": "1.22.1", "uptime_before_crash": "45 days"}',
                'network_errors': '[]',
                'js_errors': '[]',
                'days_ago': 10,
            },
            {
                'title': 'Медленная работа поиска по архиву документов',
                'description': 'Полнотекстовый поиск по архивным документам работает очень медленно (15-20 секунд на запрос). База данных содержит 500К+ документов. Требуется оптимизация индексов или переход на Elasticsearch.',
                'status': 'in_progress',
                'priority': 'medium',
                'project': 'arrfr-portal-prod',
                'reporter_name': 'Б. Гульнара',
                'reporter_email': 'b.gulnara@finreg.kz',
                'page_url': 'https://portal.finreg.kz/documents/search',
                'console_logs': '{"query_time": 18234, "documents_scanned": 523441}',
                'network_errors': '[]',
                'js_errors': '[]',
                'days_ago': 5,
            },
            {
                'title': 'Ошибка 403 Forbidden при загрузке файлов больше 10MB',
                'description': 'Пользователи не могут загружать скан-копии документов размером более 10MB. Nginx возвращает ошибку 403. Требуется увеличение лимита client_max_body_size в конфигурации.',
                'status': 'resolved',
                'priority': 'medium',
                'project': 'market-reporting-system',
                'reporter_name': 'К. Асем',
                'reporter_email': 'k.asem@kaspi.kz',
                'page_url': 'https://reports.finreg.kz/upload',
                'console_logs': '{"error": "413 Request Entity Too Large", "file_size": "12.4MB", "limit": "10MB"}',
                'network_errors': '[{"status": 413}]',
                'js_errors': '[]',
                'days_ago': 7,
            },
            {
                'title': 'Проблема с кодировкой казахских символов в PDF отчетах',
                'description': 'При генерации PDF отчетов казахские буквы ә, ө, ү, і, ғ, қ, ң, һ отображаются некорректно (кракозябры). Проблема в отсутствии казахских шрифтов в библиотеке генерации PDF.',
                'status': 'in_progress',
                'priority': 'medium',
                'project': 'market-reporting-system',
                'reporter_name': 'А. Нұрбол',
                'reporter_email': 'a.nurbol@finreg.kz',
                'page_url': 'https://reports.finreg.kz/pdf/generate',
                'console_logs': '{"error": "Font not found for character: ә"}',
                'network_errors': '[]',
                'js_errors': '[]',
                'days_ago': 4,
            },
        ]

        # Create tickets
        ticket_count = 0
        for idx, incident in enumerate(incidents_data, start=1):
            project = projects[incident['project']]
            created_at = datetime.now() - timedelta(days=incident['days_ago'])
            
            # Assign to users based on priority
            assigned_user = None
            if incident['status'] in ['in_progress', 'resolved']:
                assigned_user = random.choice(list(users.values()))

            # Map status to model choices
            status_map = {
                'new': 'NEW',
                'in_progress': 'IN_PROGRESS',
                'resolved': 'CLOSED',
            }

            ticket = Ticket.objects.create(
                project=project,
                ticket_id=f'ARRFR-{idx:04d}',
                description=f"{incident['title']}\n\n{incident['description']}",
                status=status_map[incident['status']],
                author_name=incident['reporter_name'],
                author_email=incident['reporter_email'],
                page_url=incident['page_url'],
                console_logs=incident['console_logs'],
                network_errors=incident['network_errors'],
                js_errors=incident['js_errors'],
                assigned_to=assigned_user,
                created_at=created_at,
                updated_at=created_at,
            )
            ticket_count += 1

            # Add comments for in_progress and resolved tickets
            if incident['status'] == 'in_progress':
                Comment.objects.create(
                    ticket=ticket,
                    author=assigned_user,
                    text=f'Начал работу над проблемой. Анализирую логи и воспроизвожу ошибку на тестовой среде.',
                )
            elif incident['status'] == 'resolved':
                Comment.objects.create(
                    ticket=ticket,
                    author=assigned_user,
                    text=f'Проблема решена. Внесены исправления и задеплоены на продакшн.',
                )

        self.stdout.write(self.style.SUCCESS(f'✓ Created {ticket_count} tickets with comments'))

        self.stdout.write(self.style.SUCCESS('\n' + '='*60))
        self.stdout.write(self.style.SUCCESS('Database population completed successfully!'))
        self.stdout.write(self.style.SUCCESS('='*60))
        self.stdout.write(f'Users: {len(users) + 1} (including superuser)')
        self.stdout.write(f'Projects: {len(projects)}')
        self.stdout.write(f'Tickets: {ticket_count}')
        self.stdout.write(self.style.SUCCESS('\nLogin credentials:'))
        self.stdout.write(f'  Superuser: root / 123')
        self.stdout.write(f'  Staff users: <username> / 123')
