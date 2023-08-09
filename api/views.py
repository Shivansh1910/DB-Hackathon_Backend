from django.shortcuts import render
from . import models, serializers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import datetime
# Create your views here.

# create a view for the database of user with the following fields


@api_view(['GET'])
def getUsers(request):
    users = models.DBUser.objects.all()
    user_serializer = serializers.DBUserSerializer(users, many=True)
    return Response(user_serializer.data)


@api_view(['POST'])
def getUser(request):
    reqData = request.data
    email = reqData['email']
    user = models.DBUser.objects.get(email=email)
    user_serializer = serializers.DBUserSerializer(user, many=False)
    return Response(user_serializer.data)


@api_view(['POST'])
def createUser(request):
    request_data = request.data
    user, created = User.objects.get_or_create(username=reqdata['username'])
    if created:
        try:
            user.set_password(reqdata['password'])
            user.save()

            # create DBUser
            dbuser = models.DBUser.objects.create(
                auth=user,
                name=reqdata['name'],
                email=reqdata['email'],
                handle=reqdata['handle'],
                role='employee',
                isActive=True,
                isVerified=False
            )

            return Response({
                "success": True,
                "message": "User created successfully"
            })

        except:
            user.delete()
            return Response({
                "success": False,
                "message": "Something went wrong"
            })

    else:
        return Response({
            "success": False,
            "message": "User already exists"
        })


@api_view(['POST'])
def updateUser(request):
    # update DBUser
    user = request.user
    reqdata = request.data
    dbuser = models.DBUser.objects.get(auth=user)
    dbuser.name = reqdata['name']
    dbuser.save()
    return Response({
        "success": True,
        "message": "User updated successfully"
    })


@api_view(['POST'])
def loginUser(request):
    try:
        reqdata = request.data
        username = reqdata['username']
        password = reqdata['password']
        user = User.objects.get(username=username)
        token, c = Token.objects.get_or_create(user=user)
        if user.check_password(password):
            return Response({
                "success": True,
                "message": "Login successful",
                "token": token.key,
            })
        else:
            return Response({
                "success": False,
                "message": "Invalid credentials",
                "token": None
            })
    except Exception as e:
        message = type(e).__name__ + " : " + e.args[0]
        return Response({
            "success": False,
            "message": message,
            "token": None
        })


@api_view(['GET'])
def getUserFromToken(request):
    try:
        reqUser = request.user
        print(reqUser)
        dbuser = models.DBUser.objects.get(auth=reqUser)
        user_serializer = serializers.DBUserSerializer(dbuser, many=False)
        return Response({
            "success": True,
            "message": "User fetched successfully",
            "data": user_serializer.data
        })
    except Exception as e:
        messages = type(e).__name__ + " : " + e.args[0]
        print(messages)
        return Response({
            "success": False,
            "message": "Invalid token or user does not exist",
            "data": None
        })


@api_view(['POST'])
def getNotifications(request):
    user = request.user
    dbuser = models.DBUser.objects.get(auth=user)
    notifications = models.Notification.objects.filter(user=dbuser)
    notification_serializer = serializers.NotificationSerializer(
        notifications, many=True)
    return Response({
        "success": True,
        "message": "Notifications fetched successfully",
        "notifications": notification_serializer.data
    })


@api_view(['PUT'])
def updateNotifications(request):
    user = request.user
    data = request.data
    dbuser = models.DBUser.objects.get(auth=user)
    pk = data['id']
    notification = models.Notification.objects.get(pk=pk, user=dbuser)
    notification.isRead = True
    notification.save()
    return Response({
        "success": True,
        "message": "Notification marked as read successfully"
    })


@api_view(['GET'])
def getAllSecurities(request):
    securities = models.Security.objects.all()
    security_serializer = serializers.SecuritySerializer(securities, many=True)
    return Response({
        "success": True,
        "message": "Securities fetched successfully",
        "data": security_serializer.data
    })


@api_view(['POST'])
def getSecurityByID(request):
    data = request.data
    pk = data['id']
    security = models.Security.objects.get(pk=pk)
    security_serializer = serializers.SecuritySerializer(security, many=False)
    return Response({
        "success": True,
        "message": "Security fetched successfully",
        "security": security_serializer.data
    })


@api_view(['POST'])
def getAllTradeBySecurity(request):
    data = request.data
    pk = data['id']
    security = models.Security.objects.get(pk=pk)
    trades = models.Trade.objects.filter(security=security)
    trade_serializer = serializers.TradeSerializer(trades, many=True)
    return Response({
        "success": True,
        "message": "Trades fetched successfully",
        "trades": trade_serializer.data
    })


@api_view(['POST'])
def deleteSecurity(request):
    data = request.data
    pk = data['id']
    security = models.Security.objects.get(pk=pk)
    security.delete()
    return Response({
        "success": True,
        "message": "Security deleted successfully"
    })


@api_view(['POST'])
def getTradeByID(request):
    data = request.data
    pk = data['id']
    trade = models.Trade.objects.get(pk=pk)
    trade_serializer = serializers.TradeSerializer(trade, many=False)
    return Response({
        "success": True,
        "message": "Trade fetched successfully",
        "trade": trade_serializer.data
    })


@api_view(['POST'])
def getSecurityByTrade(request):
    data = request.data
    pk = data['id']
    trade = models.Trade.objects.get(pk=pk)
    security = trade.security
    security_serializer = serializers.SecuritySerializer(security, many=False)
    return Response({
        "success": True,
        "message": "Security fetched successfully",
        "security": security_serializer.data
    })


@api_view(['GET'])
def getUserBooks(request):
    try:
        user = request.user
        dbuser = models.DBUser.objects.get(auth=user)
        books = models.UserBook.objects.filter(user=dbuser)
        book_serializer = serializers.UserBookSerializer(books, many=True)
        return Response({
            "success": True,
            "message": "Books fetched successfully",
            "data": book_serializer.data
        })
    except Exception as e:
        message = type(e).__name__ + " : " + e.args[0]
        return Response({
            "success": False,
            "message": "Something went wrong",
            "error": message,
            "data": None
        })


@api_view(['POST'])
def getAllTradeByBook(request):
    try:
        user = request.user
        data = request.data
        pk = data['id']
        book = models.Book.objects.get(pk=pk)
        dbUser = models.DBUser.objects.get(auth=user)
        userBook = models.UserBook.objects.get(user=dbUser, book=book)
        trades = models.Trade.objects.filter(book=userBook.book)
        trade_serializer = serializers.TradeSerializer(trades, many=True)
        return Response({
            "success": True,
            "message": "Trades fetched successfully",
            "data": trade_serializer.data
        })
    except Exception as e:
        message = type(e).__name__ + " : " + e.args[0]
        return Response({
            "success": False,
            "message": "Something went wrong",
            "error": message,
            "data": None
        })


@api_view(['POST'])
def reportTrade(request):
    try:
        data = request.data
        pk = data['id']
        trade = models.Trade.objects.get(pk=pk)
        report = models.Report.objects.create(
            trade=trade,
            authority=data['authority'],
            message=data['message']
        )

        trade.isReported = True
        trade.save()
        return Response({
            "success": True,
            "message": "Trade reported successfully",
            "data": None
        })
    except Exception as e:
        message = type(e).__name__ + " : " + e.args[0]
        return Response({
            "success": False,
            "message": "Something went wrong",
            "error": message,
            "data": None
        })


@api_view(['POST'])
def addToWatchlist(request):
    try:
        user = request.user
        data = request.data
        pk = data['id']
        trade = models.Trade.objects.get(pk=pk)
        dbUser = models.DBUser.objects.get(auth=user)
        watchlist, created = models.Watchlist.objects.get_or_create(
            user=dbUser, trade=trade)
        if created:
            return Response({
                "success": True,
                "message": "Security added to watchlist successfully",
                "data": None
            })
        else:
            return Response({
                "success": False,
                "message": "Security already in watchlist",
                "data": None
            })
    except Exception as e:
        message = type(e).__name__ + " : " + e.args[0]
        return Response({
            "success": False,
            "message": "Something went wrong",
            "error": message,
            "data": None
        })


@api_view(['POST'])
def deleteFromWatchlist(request):
    try:
        user = request.user
        data = request.data
        pk = data['id']
        trade = models.Trade.objects.get(pk=pk)
        dbUser = models.DBUser.objects.get(auth=user)
        watchlist = models.Watchlist.objects.get(
            user=dbUser, trade=trade
        )
        watchlist.delete()
        return Response({
            "success": True,
            "message": "Security deleted from watchlist successfully",
            "data": None
        })
    except Exception as e:
        message = type(e).__name__ + " : " + e.args[0]
        return Response({
            "success": False,
            "message": "Something went wrong",
            "error": message,
            "data": None
        })


@api_view(['GET'])
def getAllTradeByWatchList(request):
    try:
        user = request.user
        dbUser = models.DBUser.objects.get(auth=user)
        watchlist = models.Watchlist.objects.filter(user=dbUser)
        trades = []
        for item in watchlist:
            trades.append(item.trade)
        trade_serializer = serializers.TradeSerializer(trades, many=True)
        return Response({
            "success": True,
            "message": "Trades fetched successfully",
            "data": trade_serializer.data
        })
    except Exception as e:
        message = type(e).__name__ + " : " + e.args[0]
        return Response({
            "success": False,
            "message": "Something went wrong",
            "error": message,
            "data": None
        })


@api_view(['GET'])
def dashboard(request):
    user = request.user
    dbuser = models.DBUser.objects.get(auth=user)
    userBooks = models.UserBook.objects.filter(user=dbuser)
    trades = []
    for userBook in userBooks:
        trades += models.Trade.objects.filter(book=userBook.book)

    totalTrades = len(trades)
    # get value of totalTrades by iterating through trades
    volume = 0
    for trade in trades:
        volume += trade.price * trade.quantity

    critialTrades = 0
    mediumRisk = 0
    today = datetime.date.today()

    # create dict with bookname and value 0
    critialDistribution = {}
    for userBook in userBooks:
        critialDistribution[userBook.book.name] = 0

    settlementDistribution = {}
    settlementDistributionByYear = {}
    for trade in trades:
        try:
            settlementDistribution[trade.settlementDate.strftime(
                "%Y-%m-%d")] += 1
        except:
            settlementDistribution[trade.settlementDate.strftime(
                "%Y-%m-%d")] = 1

        try:
            settlementDistributionByYear[trade.settlementDate.strftime(
                "%Y")] += trade.quantity * trade.price
        except:
            settlementDistributionByYear[trade.settlementDate.strftime(
                "%Y")] = trade.quantity * trade.price

        if trade.settlementDate < today or trade.settlementDate < trade.security.maturityDate:
            critialTrades += 1
            critialDistribution[trade.book.name] += 1
        elif trade.settlementDate > today and today > trade.security.maturityDate:
            mediumRisk += 1
        else:
            pass

    return Response({
        "success": True,
        "message": "Dashboard fetched successfully",
        "data": {
            "totalTrades": totalTrades,
            "volume": volume,
            "critialTrades": critialTrades,
            "mediumRisk": mediumRisk,
            "critialDistribution": critialDistribution,
            "settlementDistribution": settlementDistribution,
            "settlementDistributionByYear": settlementDistributionByYear
        }
    })


@api_view(['POST'])
def searchRelatedSecutity(request):
    # get all securities from database with ISIN related to the search query
    data = request.data
    searchQuery = data['searchQuery']
    securities = models.Security.objects.filter(ISIN__icontains=searchQuery)
    security_serializer = serializers.SecuritySerializer(securities, many=True)
    return Response({
        "success": True,
        "message": "Securities fetched successfully",
        "data": security_serializer.data
    })
